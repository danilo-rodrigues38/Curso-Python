try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except ZeroDivisionError:
    print('\n\033[31mImpossível divisão por zero!\033[m')
except ValueError:
    print('\n\033[31mDados informados incorretos!'
          '\nDigite somente números inteiros.\033[m')
except KeyboardInterrupt:
    print('\n\n\033[31mO usuário interrompeu a execução!\033[m')
except Exception as erro:
    print(f'\nO problema encontrado foi {erro.__class__}')
else:
    print(f'\nO resultado é {r:.1f}')
finally:
    print('\n\033[1;3;32mVolte sempre! Muito Obrigado!\033[m')
