import subprocess
subprocess.check_output(["scrapy", "crawl", "pydoc", "-o", "pydocTest.jl"], cwd="./python_scraping2")
