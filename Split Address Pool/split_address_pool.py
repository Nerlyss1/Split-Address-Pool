import ipaddress

def calculate_subnet_mask(num_addresses):
    # Trouver le masque de sous-réseau approprié en fonction du nombre d'adresses demandées
    mask_length = 32 - (num_addresses.bit_length() - 1)
    return "/" + str(mask_length)

def split_address_pool(pool_address, num_addresses_per_subnet):
    pool_network = ipaddress.IPv4Network(pool_address, strict=False)
    subnets = []

    for num_addresses in num_addresses_per_subnet:
        subnet_mask = calculate_subnet_mask(num_addresses)
        subnet = list(pool_network.subnets(new_prefix=subnet_mask))
        if subnet:
            subnets.append(subnet.pop(0))

    return subnets

if __name__ == "__main__":
    pool_network = input("Entrez l'adresse IP du pool (ex. 192.168.0.0/24): ")

    num_subnets = int(input("Combien de sous-réseaux souhaitez-vous créer ? "))
    num_addresses_per_subnet = []

    for i in range(num_subnets):
        num_addresses = int(input(f"Combien d'adresses voulez-vous pour le sous-réseau {i+1} ? "))
        num_addresses_per_subnet.append(num_addresses)

    subnets = split_address_pool(pool_network, num_addresses_per_subnet)

    print("Les sous-réseaux découpés sont :")
    for i, subnet in enumerate(subnets):
        subnet_mask = calculate_subnet_mask(num_addresses_per_subnet[i])
        print(f"Le sous-réseau {i+1} : {subnet}/{subnet_mask}")
