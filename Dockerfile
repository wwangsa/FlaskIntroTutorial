#Creating docker file for flaskintroduction project
# Docker Flask Tutorial: https://medium.com/@doedotdev/docker-flask-a-simple-tutorial-bbcb2f4110b5
# Github: https://github.com/wwangsa/FlaskIntroTutorial
# Docker hub: https://hub.docker.com/r/wwangsa/flask_intro
FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#As it define in the from line, it will use python 3.8, there is no need to call python3 on entrypoint.
ENTRYPOINT ["python"]
CMD ["app.py"]
