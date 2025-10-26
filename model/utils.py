def show_tree(jwt_string):
    header, payload, signature = jwt_string.split('.')
    print("JWT")
    print("├── HEADER:    ", header)
    print("├── PAYLOAD:   ", payload)
    print("└── SIGNATURE: ", signature)
    # Salida esperada:
    # JWT