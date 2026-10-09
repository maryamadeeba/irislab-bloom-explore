IRISLAB — BLOOM & EXPLORE
========================

This bundle connects the flower-themed dashboard to the CURRENT dataframe from
Task_1_Iris_EDA.ipynb through a CSV bridge. The server re-reads iris_data.csv on
every API request and the browser refreshes the display every 5 seconds.

FILES
- irislab_frontend_connected.html  Flower-garden themed dashboard
- iris_dashboard_server.py         Flask API, reads iris_data.csv live
- requirements_iris_dashboard.txt  Python dependencies
- Task_1_Iris_EDA.ipynb             Your EDA notebook with an export cell appended

SETUP (Windows / VS Code)
1. Extract the ZIP into a folder.
2. Put Task_1_Iris_EDA.ipynb in that same folder as the three dashboard files.
   (The notebook is supplied separately with your upload; the ZIP may include a
   copy if you package it together.)
3. Open the notebook in Jupyter or VS Code and run its cells in order.
4. Run the final cell titled “Publish the live dashboard dataset”. It exports the
   current notebook dataframe to iris_data.csv in the notebook's current working
   directory. For simplest setup, set the notebook working directory to this folder.
5. In a terminal opened in the folder containing iris_dashboard_server.py, install:
       py -m pip install -r requirements_iris_dashboard.txt
   If `py` is unavailable, use `python -m pip install -r requirements_iris_dashboard.txt`.
6. Start the API:
       py iris_dashboard_server.py
   Or `python iris_dashboard_server.py`.
7. Open http://127.0.0.1:5000 in your browser.

HOW LIVE UPDATES WORK
- Edit/clean/filter `df` in the notebook.
- Run the final export cell again. It overwrites iris_data.csv.
- The running API reads the CSV fresh on each request, and the dashboard polls
  every 5 seconds. Updated counts, missing-value metric, species distribution,
  sample table and scatter plot will update automatically.
- If iris_data.csv does not exist yet, the API falls back to scikit-learn's built-in
  Iris dataset. The dashboard will then reflect the CSV after you export it.
- The notebook and dashboard are separate processes; the browser cannot read the
  notebook's in-memory variables directly. The CSV export is the bridge.

TROUBLESHOOTING
- If the UI stays on the fallback data, check that iris_data.csv is in the same
  directory as iris_dashboard_server.py and rerun the notebook export cell.
- If you edit the notebook dataframe, remember to rerun the export cell.
- Check http://127.0.0.1:5000/api/health to confirm the server is running.
