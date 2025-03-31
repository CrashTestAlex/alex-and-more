# Welcome

Hello! Welcome to Alex's BallsDex Cog Package Add-On or whatever! The contents of the files that are in this repo are not meant to harm you or anyone else's device in any way, so dont be afraid. 
This packages is for your Ballsdex clone. If you dont know how to install it, I suggest heading over to the [external-package-example](https://github.com/Ballsdex-Team/external-package-example)
repo that the BallsDex-Team has that shows you the instructions to make and install packages!

# BrawlPedia

> [![BrawlPedia Discord](https://discord.com/api/guilds/1270818465326043292/embed.png?style=banner2)](https://discord.gg/6jtJShmTRS)
> 
> 
> This bot is all about catching, opening & trading Brawl Stars Characters! 
> (It's NOT MEANT TO MIMIC BrawlDex, a bot made by AngerRandom)
> Invite BrawlPedia to your servers [here](https://discord.com/api/oauth2/authorize?client_id=1320555542497853543&permissions=537193536&scope=bot%20applications.commands)!

# BallsDex

> [![BallsDex Discord](https://discord.com/api/guilds/1049118743101452329/embed.png?style=banner2)](https://discord.gg/Qn2Rkdkxwc)
> 
> BallsDex is a bot where you can catch and trade countryballs! Its what inspired BrawlPedia & where BrawlPedia got most of its code from!
> Invite BallsDex to your servers [here](https://discord.com/api/oauth2/authorize?client_id=999736048596816014&permissions=537193536&scope=bot%20applications.commands)!


## Installing

Just to go over how to install, heres if you're not using docker:

### Step 1:
Run this command: 

`poetry add -n git+https://github.com/CrashTestAlex/alex-and-more.git`

### Step 2:
Go to your bots `config.yml` and find the area where it says:
    
```diff
        # list of packages that will be loaded
        packages:
            - ballsdex.packages.admin
            - ballsdex.packages.balls
            - ballsdex.packages.config
            - ballsdex.packages.countryballs
            - ballsdex.packages.info
            - ballsdex.packages.players
            - ballsdex.packages.trade
        +   - ballsdex.packages.stuffs
```

Add under your last added package, this package! Even shows the name right there, isn't that nifty?

### Step 3: 
Turn your bot back on again & watch the magic happen! 


## If you ARE using Docker...


Edit the file `Dockerfile` and add this line:

```diff
  COPY . /code
  RUN mkdir -p /code/static
  RUN mkdir -p /code/static/uploads

+ RUN pip install --upgrade --force-reinstall git+https://github.com/CrashTestAlex/alex-and-more.git

  # wait for postgres to be ready
  CMD sleep 2
```

Then run `docker compose build`!

## Suggestions

If you want to make any suggestions, additions, bug reports or issues, feel absolutely free to do so by making an issue on this very repo!

## Documentation

Learn how to use dex bots & packages by reading over the BallsDex repo wiki pages!
[This is a Wiki. Click me!](https://github.com/laggron42/BallsDex-Discordbot/wiki)

## Special Thanks

@hippopotis on discord for art
@ihailthenight1234 on discord for help with coding
@newzac. on discord for A LOT OF HELP with coding

## License

This repository is released under the [MIT license](https://opensource.org/licenses/MIT).

If distributing this package, credits to the original authors must not be removed.