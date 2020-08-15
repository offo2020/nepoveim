#ale predsa spravim zmenu
nebran mi kamarat

zmeny pre vetvu, aj som zmazal 'co ked budem'

'''
taky kodik ty pylint prisny
'''

def function():
    '''
    chce integer a da na druhu
    '''

    while True:
        try:
            num = int(input('Daj cele cislo chuju!: '))    
        except:
            print('to nebolo cele cislo, ze? Znova kamosko!')
            continue
        else:
            break
    print('jeho druha mocnina je: ', num**2)

function()