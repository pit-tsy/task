import train
import generate

train.fit()
with open('generated_text.txt', 'w', encoding='windows-1251') as file:
    file.write(generate.gen())
