import random

P = 65537
G = 17

def generate_private_key():
    return random.randint(2, P-2)

def compute_public_key(private_key):
    return pow(G, private_key, P)

def compute_shared_secret(public_key, private_key):
    return pow(public_key, private_key, P)

if __name__ == "__main__":
    alice_private = generate_private_key()
    alice_public = compute_public_key(alice_private)

    bob_private = generate_private_key()
    bob_public = compute_public_key(bob_private)

    alice_shared = compute_shared_secret(bob_public, alice_private)
    bob_shared = compute_shared_secret(alice_public, bob_private)

    print(f"Alice's Shared Key: {alice_shared}")
    print(f"Bob's Shared Key: {bob_shared}")
