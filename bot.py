import json

import discord
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('$'):
        msg = message.content[1::]
        msg_list = msg.split('-')
        print(msg_list)
        r = requests.post('https://api.imgflip.com/caption_image', 
            data={
                'template_id': int(msg_list[0]),
                'username': IMGFLIP_USER,
                'password': IMGFLIP_PASS,
                'text0': msg_list[1],
                'text1': msg_list[2],
            })
        print(r.json())
        print(r.status_code)
        ret_json = r.json()
        if ret_json['success'] == True:
            await message.channel.send(ret_json['data']['url'])

with open('config.json') as json_file:
    json_dict = json.load(json_file)
API_KEY = json_dict['API_KEY']
IMGFLIP_USER = json_dict['imgflip_user']
IMGFLIP_PASS = json_dict['imgflip_pass']

client.run(json_dict['API_KEY'])