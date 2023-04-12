import discord


class D_Embeds:
    def __init__(self):
        pass

    def pass_embed(self, text):
        em = discord.Embed(
            color=discord.Color.from_rgb(0, 255, 0),
            title="Completado",
            description=text,
        )
        return em

    def fail_embed(sekf, text):
        em = discord.Embed(
            color=discord.Color.from_rgb(255, 0, 0),
            title="Error",
            description=text,
        )
        return em
