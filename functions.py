def get_summ(one, two, delimiter='&') -> str:
    return f'{one}{delimiter}{two}'

var = get_summ("Learn", "python")
print(var.upper())
