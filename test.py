from bases.physics.box_collider import BoxCollider

if __name__ == "__main__":
    bc1 = BoxCollider(20, 20)
    bc2 = BoxCollider(10, 30)

    bc1.position.x + 10

    print(bc1.collide_with(bc2)) 