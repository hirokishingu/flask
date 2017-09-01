import subprocess
subprocess.check_output(["scrapy", "crawl", "pydoc", "-o", "pydocccTest.jl"], cwd="./python_scraping2")
