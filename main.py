from telegram.ext import Updater, CommandHandler

# Define your command handler
def sds_command(update, context):
    message = (
        "@queenasteisha @butterscotch25 @arinakozak @krumushka @mr_dr_73 @ksushandikk "
        "@tmshnko @clownwithoutcircus @sofaaaaya @ann_chub @elickkk @anastasikates "
        "@milkywayeva @fdrshkn @aminamedzhidova @iraarii @fyxulazz "
        "@thedeadgirlinthepool @brightsunrise8 @nav1kk @verrtvd @luersire @skurelen "
        "@kreechkaa @whos9tkin @lkyzh @an_z_annnn @ilubebe @dashajim @dsyrrnik @a_echka "
        "@washasasha."
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Main function to set up the bot
def main():
    # Replace 'YOUR_API_TOKEN' with your bot's API token
    updater = Updater("7277265053:AAGHYcMa964trUKVHroYeKRMVdgOXpwbxro", use_context=True)
    dp = updater.dispatcher

    # Add the /sds command handler
    dp.add_handler(CommandHandler("sds", sds_command))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
