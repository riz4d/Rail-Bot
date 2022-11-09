#©Mohamed Rizad
#09112022
import requests as re
from Config import *
from pyrogram import *

bot=Client('Rail-Bot',
       api_id=API_ID,
       api_hash=API_HASH,
       bot_token=BOT_TOKEN)
@bot.on_message(filters.command('start'))
async def start_msg(client,message):
    await message.reply("Hey! I'm is RailBot. I can retrieves you details about railway status using.send /help to know how to use me.")
    
    
@bot.on_message(filters.text)
async def rail_info(client,message):
    mess=str(message.text)
    print(mess)
    
    if '/gettraininfo ' in mess:  
      m=mess.lstrip('/gettraininfo ')
      print(m)
      url='https://india-rail.herokuapp.com/trains/getTrain/?trainNo='+m
      res=re.get(url)
      try:
         infojs=res.json()['data']
         train_no=infojs['train_no']
         train_name=infojs['train_name']
         from_stn_name=infojs['from_stn_name']
         from_stn_code=infojs['from_stn_code']
         to_stn_name=infojs['to_stn_name']
         to_stn_code=infojs['to_stn_code']
         from_time=infojs['from_time']
         to_time=infojs['to_time']
         travel_time=infojs['travel_time']
         running_days=infojs['running_days']
         typ=infojs['type']
         train_id=infojs['train_id']
         distance_from_to=infojs['distance_from_to']
         average_speed=infojs['average_speed']
         
         data="<b>Fetched Data's</b>"+'\n\n'+'Train No : __'+train_no+'__\nTrain Name : __'+train_name+'__\nTrain ID : __'+train_id+'__\nTrain Type : __'+typ+'__\nAverage Speed : __'+average_speed+'__\nFrom Station name : __'+from_stn_name+'__\nFrom Station Code : __'+from_stn_code+'__\nTo Station : __'+to_stn_name+'__\nTo Station Code : __'+to_stn_code+'__\nTotal Distance : __'+distance_from_to+'__\nDeparture : __'+from_time+'__\nArrival : __'+to_time+'__\nTravel Time : __'+travel_time+' Hrs\nRunning Days : __'+running_days
   
         await message.reply(data)
      except:
          await message.reply('Invalid Train Number\n\nFormat : `/gettraininfo 22638')
    elif '/getroute ' in mess:
        j=mess.lstrip('/getroute ')
        routeurl='https://india-rail.herokuapp.com/trains/getRoute?trainNo='+j
        routeres=re.get(routeurl)
        js=routeres.json()['data']
        
        a=''
        try:
           for i in js:
               Source_stn=i['source_stn_name']
               Source_stncd=i['source_stn_code']
               arrive=i['arrive']
               depart=i['depart']
               distance=i['distance']
               day=i['day']
               zone=i['zone']
               n='Station : '+Source_stn+'\nStation Code : '+Source_stncd+'\nArrival : '+arrive+'\nDeparture : '+depart+'\nDistance : '+distance+' km\nDays : '+day+'\nZone'+zone+'\n\n      ↓  \n\n'
               await message.reply(n)
        except:
            await message.reply('Invalid Train Number\n\nFormat : `/getroute 22638')
    #github @riz4d
    elif '/gettrain ' in mess:
        k=mess.replace('/gettrain ','')
        burl='https://india-rail.herokuapp.com/trains/betweenStations/?from='
        fr=k.replace('-', '&to=')
        url=burl+fr
        res=re.get(url)
        jss=res.json()['data']
        print(url)
        print(k)
        print(mess)
        try:
          for x in jss:
              infox=x['train_base']
              train_no=infox['train_no']
              train_name=infox['train_name']
              source_stn_name=infox['source_stn_name']
              source_stn_code=infox['source_stn_code']
              dstn_stn_name=infox['dstn_stn_name']
              dstn_stn_code=infox['dstn_stn_code']
              from_stn_name=infox['from_stn_name']
              from_stn_code=infox['from_stn_code']
              to_stn_name=infox['to_stn_name']
              to_stn_code=infox['to_stn_code']
              from_time=infox['from_time']
              to_time=infox['to_time']
              travel_time=infox['travel_time']
              running_days=infox['running_days']
                  
              xinfo='\n  <b>'+train_name+'</b>  \n\nTrain No : __'+train_no+'__\nTrain Name : __'+train_name+'__\nSource Station : __'+source_stn_name+'__\nSource Station Code : __'+source_stn_code+'__\nDestination Station : __'+dstn_stn_name+'__\nDestination Station Code :'+dstn_stn_code+'__\nFrom Station name : __'+from_stn_name+'__\nFrom Station Code : __'+from_stn_code+'__\nTo Station : __'+to_stn_name+'__\nTo Station Code : __'+to_stn_code+'__\nDeparture : __'+from_time+'__\nArrival : __'+to_time+'__\nTravel Time : __'+travel_time+' Hrs\nRunning Days : __'+running_days   
              await message.reply(xinfo)
        except:
            await message.reply('Invalid Station or Format\n\nFormat : `/gettrain ed-kcg`')
    else:
        await message.reply("I think🤔 you didn't know how to use me")
        await message.reply("Don't Worry just keep this format\n\n→ `/gettraininfo 22638` : Retrieves Information about the train\n\n→ `/getroute 22638` : Retrieves Information about the route of the train\n\n→ `/gettrain ed-maq` : Retrieves available trains between the stations")
        await message.reply('Further Queries @riz4d')
#Telegram @riz4d
bot.run()
