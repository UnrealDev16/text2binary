def main():
    text=input("Enter Text ")
    final=[]
    ascii=[]
    for character in text:
        final.append(bin(ord(character))[2:])
        ascii.append(ord(character))
        asout=' '.join(map(str,ascii))
        output=' '.join(final)
    print(asout)
    print(output)
    main()
main()