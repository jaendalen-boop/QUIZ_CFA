@echo off
cd /d "%~dp0"

echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo Lancement de Streamlit avec le Python du venv...
venv\Scripts\python.exe -m streamlit run app.py

echo.
echo Fin du script. Appuyez sur une touche pour fermer.
pause >nul
