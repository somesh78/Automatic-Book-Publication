from workflows.pipeline import run_pipeline

if __name__ == "__main__":
    URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    run_pipeline(URL, "chapter1_v1")
