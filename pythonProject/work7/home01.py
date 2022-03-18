#鸡兔同笼:60只、180脚，各多少只？
for chicken in range ( 0, 60 ):
    rabbit = 60 - chicken
    chickLeg = 2 * chicken
    rabLeg = 4 * rabbit

    if (chickLeg + rabLeg == 180):
      print ( "鸡{0} 兔{1}".format ( str ( chicken ), str ( rabbit ) ) )