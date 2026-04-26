from flask import Flask, render_template, request # render_template 추가

# ... (스크래핑 함수들은 동일) ...

@app.route("/")
def home():
    return render_template("index.html") # HTML 파일 렌더링

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if not keyword:
        return redirect("/")
    
    # 스크래핑 실행
    all_jobs = scrape_berlin(keyword) + scrape_web3(keyword) + scrape_wework(keyword)
    
    # 템플릿에 데이터 전달
    return render_template("search.html", keyword=keyword, jobs=all_jobs)
