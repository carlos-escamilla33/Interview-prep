def asteriodCollision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        while stack and asteroid < 0 and stack[-1] > 0:
            if abs(asteroid) > stack[-1]:
                stack.pop()
                continue
            elif abs(asteroid) == stack[-1]:
                stack.pop()
            asteroid = 0
            break
        if asteroid != 0:
            stack.append(asteroid)
    
    return stack

asteroids = [3,5,-6,2,-1,4]

print(asteriodCollision(asteroids))