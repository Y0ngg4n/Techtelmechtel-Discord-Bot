FROM python:3.7-slim

RUN apt update && apt install -y python3-pip git
RUN mkdir -p /opt/discord
RUN git clone https://github.com/Y0ngg4n/Techtelmechtel-Discord-Bot.git /opt/discord/techtelmechtel
RUN cd /opt/discord/techtelmechtel && pip install -r requirements.txt
WORKDIR /opt/discord/techtelmechtel
CMD ["'/bin/bash' '-c' 'echo DISCORD_TOKEN=${BOT_TOKEN} > /opt/discord/techtelmechtel/.env && python /opt/discord/techtelmechtel/Main.py'"]