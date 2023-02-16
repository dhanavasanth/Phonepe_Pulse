<video height = "200" src = "https://user-images.githubusercontent.com/117557948/219284713-df4c0aa8-af61-4a48-b1b5-0bd1c83aadcc.mp4"></video> 

<h1 align="center"> Phonepe_Pulse Data Visualisation using "SQLite"</h1>

<img align="right" alt="Coding" width="300" src="https://media.giphy.com/media/vISmwpBJUNYzukTnVx/giphy.gif">


## Deployment

To deploy this project run

```bash
  import streamlit as st
  from PIL import Image
  import os
  import json
  from streamlit_option_menu import option_menu
  import subprocess
  import plotly.express as px
  import pandas as pd
  import sqlite3
  import requests
```

## Cloning phonepe pulse Repository

```bash
  response = requests.get('https://api.github.com/repos/PhonePe/pulse')
  repo = response.json()
  clone_url = repo['clone_url']

  repo_name = "pulse"
  clone_dir = os.path.join(os.getcwd(), repo_name)
```
## Creating  Data-Tables 

After Cloning Git-hub create a corresponding DataFrame of given pulse data's and insert it into SQL database and create diffrent tables for diffrent aggregated data's 

![screen_table](https://user-images.githubusercontent.com/117557948/219296120-3268153c-22f4-408c-8443-88d870ecddfe.png)


## Create SQL queries to fetch corresponding Data's

```python
SELECT * FROM "Table"
WHERE "Condition"
GROUP BY "Columns"
ORDER BY "Data"
```



    


