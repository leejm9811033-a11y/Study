from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from db import insert_survey, fetchall_survey
from analysis import analysis_func, save_barchart_func
import time

BASE_DIR = Path(__file__).resolve().parent
IMG_PATH = BASE_DIR / "static" / "images" / "vbar.png"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/coffee/survey")
def survey_view():
    return render_template("coffee/coffeesurvey.html")

@app.post("/coffee/surveyprocess")
def surveyprocess():
    gender = (request.form.get("gender") or "").strip()
    age_raw = (request.form.get("age") or "").strip()
    co_survey = (request.form.get("co_survey") or "").strip()

    if not gender or not co_survey or not age_raw.isdigit():
        return redirect(url_for("survey_view"))

    age = int(age_raw)

    insert_survey(gender=gender, age=age, co_survey=co_survey)

    rdata = fetchall_survey()
    crossTab, results, df = analysis_func(rdata)

    if not df.empty:
        save_barchart_func(df, IMG_PATH)

    return render_template(
        "coffee/result.html",
        crossTab=crossTab.to_html(classes="table table-bordered") if not crossTab.empty else "",
        results=results,
        df=df.to_html(classes="table table-striped", index=False) if not df.empty else "",
        img_url=url_for("static", filename="images/vbar.png", v=int(time.time()))
    )

@app.get("/coffee/surveyshow")
def surveyshow():
    rdata = fetchall_survey()
    crossTab, results, df = analysis_func(rdata)

    if not df.empty:
        save_barchart_func(df, IMG_PATH)

    return render_template(
        "coffee/result.html",
        crossTab=crossTab.to_html(classes="table table-bordered") if not crossTab.empty else "",
        results=results,
        df=df.to_html(classes="table table-striped", index=False) if not df.empty else "",
        img_url=url_for("static", filename="images/vbar.png", v=int(time.time()))
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)