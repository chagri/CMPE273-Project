import enchant


def SpellCheckResponse(check_spleeing):

    d = enchant.Dict("en_US")
    return  d.check(check_spleeing)



