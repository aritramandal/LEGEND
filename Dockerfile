"imported from Eliza by peru_monster"

FROM suhaash02/eliza:latest

#clonning repo 

RUN git clone https://github.com/aritramandal/LEGEND.git /root/userbot

#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
