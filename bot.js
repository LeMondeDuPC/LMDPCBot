const Discord = require('discord.js');
const Config = require('./config.json');
const Client = new Discord.Client();

Client.on('ready', () => {
    console.log(`Logged in as ${Client.user.tag}!`);
});

// commandes
Client.on('message', message => {
    let channel = message.guild.channels.cache.find(ch => ch.name === '💻commandes');
    if(channel){
        if (!message.content.startsWith(Config.prefix) || message.author.bot){
            return;
        }
        if(message.content.startsWith(Config.prefix+'help')){

        }
        if(message.content.startsWith(Config.prefix+'subscribe')){
            let member = message.member;
            let role = message.guild.roles.cache.find(r => r.name === 'Abonné');
            member.roles.add(role.id);
            channel.send('ok');
        }
        if(message.content.startsWith(Config.prefix+'unsubscribe')){
            let member = message.member;
            let role = message.guild.roles.cache.find(r => r.name === 'Abonné');
            member.roles.remove(role.id);
            channel.send('ok');
        }
    }
});

// bienvenue
Client.on("guildMemberAdd", (member) => {
    let channel = member.guild.channels.cache.find(ch => ch.name === '🌍bienvenue');
    if(channel){
        let role = message.guild.roles.cache.find(r => r.name === 'Membre');
        member.roles.add(role.id)
        channel.send('Bienvenue '+member+' ! \n' +
            '\n' +
            'Allez dans #📌présentation  pour en apprendre plus sur notre projet : Le Monde Du PC ! ');

    }
});

Client.login(Config.token);