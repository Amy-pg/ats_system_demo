from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from datetime import datetime
from flask import send_file

app = Flask(__name__)

@app.route("/")
def index():
    csv_path = os.path.join("data", "dummy_jobs.csv")
    jobs_df = pd.read_csv(csv_path, encoding="utf-8")
    jobs = jobs_df.to_dict(orient="records")
    return render_template("jobs.html", jobs=jobs)

@app.route("/apply", methods=["GET", "POST"])
def apply():
    job_csv = os.path.join("data", "dummy_jobs.csv")
    jobs_df = pd.read_csv(job_csv, encoding="utf-8")
    jobs = jobs_df.to_dict(orient="records")

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        job_id = request.form["job_id"]
        message = request.form["message"]

        # 保存先CSV
        applicant_csv = os.path.join("data", "applicants.csv")
        df = pd.DataFrame([{
            "name": name,
            "email": email,
            "job_id": job_id,
            "message": message,
            "apply_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "選考中"  # 初期ステータス
        }])
        df.to_csv(applicant_csv, mode="a", header=not os.path.exists(applicant_csv), index=False)


        return redirect(url_for("thank_you"))

    return render_template("apply.html", jobs=jobs)

@app.route("/thank_you")
def thank_you():
    return render_template("thank_you.html")

@app.route("/applicants")
def applicants():
    applicant_csv = os.path.join("data", "applicants.csv")
    if not os.path.exists(applicant_csv):
        return "応募者データがありません"

    df = pd.read_csv(applicant_csv)
    applicants = df.to_dict(orient="records")
    return render_template("applicants.html", applicants=applicants)

@app.route("/applicant/<int:index>", methods=["GET", "POST"])
def applicant_detail(index):
    applicant_csv = os.path.join("data", "applicants.csv")
    df = pd.read_csv(applicant_csv)

    if index >= len(df):
        return "応募者が見つかりません"

    applicant = df.iloc[index].to_dict()

    if request.method == "POST":
        # 更新処理
        new_status = request.form["status"]
        new_memo = request.form["memo"]
        df.at[index, "status"] = new_status
        df.at[index, "memo"] = new_memo
        df.to_csv(applicant_csv, index=False)
        return redirect(url_for("applicants"))

    return render_template("applicant_detail.html", applicant=applicant, index=index)

@app.route("/applicants/download")
def download_applicants():
    applicant_csv = os.path.join("data", "applicants.csv")
    if os.path.exists(applicant_csv):
        return send_file(applicant_csv, as_attachment=True)
    else:
        return "応募者データがありません"



if __name__ == "__main__":
    app.run(debug=True)
