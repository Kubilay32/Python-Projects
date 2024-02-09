[(x0,y0),(x1,y1),(x2,y2),(x3,y3)] = eval(input())

a = max(x0,x1,x2,x3)
b = min(x0,x1,x2,x3)

if y0 >= 0 and y1 >= 0 and y2 >= 0 and y3 >= 0:
	if a == x0 == x2 and b == x3:
		area = (1/2) * abs(((x2 * 0) + (x2 * 0) + (x3 * y3) + (x3 * y2) - (y2 * x2) - (0 * x3) - (0 * x3) - (y3 * x2)))

	elif a == x1 and b == x2 == x0:
		area = (1/2) * abs(((x2 * y1) + (x1 * 0) + (x1 * 0) + (x2 * y2) - (y2 * x1) - (y1 * x1) - (0 * x2) - (0 * x2)))

	elif a == x1 == x3 and b == x0:
		area = 1/2 * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x3) - (0 * x0) - (0 * x0)))

	elif a == x1 and b == x0 == x2:
		area = 1/2 * abs(((x2 * y1) + (x1 * 0) + (x1 * 0) + (x2 * y2) - (y2 * x1) - (y1 * x1) - (0 * x2) - (0 * x2)))	
	
	elif a == x1 == x3 and b == x2:
		area = 1/2 * abs(((x2 * y1) + (x1 * 0) + (x1 * 0) + (x2 * y2) - (y2 * x1) - (y1 * x1) - (0 * x2) - (0 * x2)))

	elif a == x3 and b == x0 == x2:
		area = 1/2 * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x3) - (0 * x0) - (0 * x0)))	
	
	elif a == x0 == x2 and b == x1:
		area = 1/2 * abs(((x1 * y0) + (x0 * 0) + (x0 * 0) + (x1 * y1) - (y1 * x0) - (y0 * x0) - (0 * x1) - (0 * x1)))

	elif a == x3 and b == x1:
		area = (1/2) * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x1 * y1) + (x1 * y0) - (y0 * x3) - (y3 * x3) - (0 * x1) - (0 * x1) - (y1 * x0)))

	elif a == x2 and b == x1:
		area = (1/2) * abs(((x0 * y3) + (x3 * y2) + (x2 * 0) + (x2 * 0) + (x1 * y1) + (x1 * y0) - (y0 * x3) - (y3 * x2) - (y2 * x2) - (0 * x1) - (0 * x1) - (y1 * x0)))

	elif a == x0 and b == x1:
		area = (1/2) * abs(((x0 * 0) + (x0 * 0) + (x1 * y1) + (x1 * y0) - (y0 * x0) - (0 * x1) - (0 * x1) - (y1 * x0)))

	elif a == x1 and b == x0:
		area = (1/2) * abs(((x0 * y3) + (x3 * y2) + (x2 * y1) + (x1 * 0) + (x1 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x2) - (y2 * x1) - (y1 * x1) - (0 * x0) - (0 * x0)))

	elif a == x3 and b == x2:
		area = (1/2) * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x2 * y2) + (x2 * y1) + (x1 * y0) - (y0 * x3) - (y3 * x3) - (0 * x2) - (0 * x2) - (y2 * x1) - (y1 * x0)))

	elif a == x0 and b == x2:
		area = (1/2) * abs(((x0 * 0) + (x0 * 0) + (x2 * y2) + (x2 * y1) + (x1 * y0) - (y0 * x0) - (0 * x2) - (0 * x2) - (y2 * x1) - (y1 * x0)))

	elif a == x2 and b == x0:
		area = (1/2) * abs(((x0 * y3) + (x3 * y2) + (x2 * 0) + (x2 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x2) - (y2 * x2) - (0 * x0) - (0 * x0)))

	elif a == x0 and b == x3: 
		area = (1/2) * abs(((x0 * 0) + (x0 * 0) + (x3 * y3) + (x3 * y2) + (x2 * y1) + (x1 * y0) - (y0 * x0) - (0 * x3) - (0 * x3) - (y3 * x2) - (y2 * x1) - (y1 * x0)))

	elif a == x3 and b == x0:
		area = (1/2) * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x3) - (0 * x0) - (0 * x0)))

	elif a == x1 and b == x3:
		area = (1/2) * abs(((x3 * y2) + (x2 * y1) + (x1 * 0) + (x1 * 0) + (x3 * y3) - (y3 * x2) - (y2 * x1) - (y1 * x1) - (0 * x3) - (0 * x3)))

	elif a == x1 and b == x2:
		area = (1/2) * abs(((x2 * y1) + (x1 * 0) + (x1 * 0) + (x2 * y2) - (y2 * x1) - (y1 * x1) - (0 * x2) - (0 * x2)))

	elif a == x2 and b == x3:
		area = (1/2) * abs(((x3 * y2) + (x2 * 0) + (x2 * 0) + (x3 * y3) - (y3 * x2) - (y2 * x2) - (0 * x3) - (0 * x3)))

elif y0 <= 0 and y1 <= 0 and y2 <= 0 and y3 <= 0:
	if a == x0 and b == x1 == x3:
		area = (1/2) * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x3) - (0 * x0) - (0 * x0)))
	elif a == x3 and b == x0  == x2:
		area = 1/2 * abs(((x3 * y2) + (x2 * 0) + (x2 * 0) + (x3 * y3) - (y3 * x2) - (y2 * x2) - (0 * x3) - (0 * x3)))

	elif a == x0 and b == x1 == x3:
		area = 1/2 * abs(((x0 * y3) + (x3 * 0) + (x3 * 0) + (x0 * y0) - (y0 * x3) - (y3 * x3) - (0 * x0) - (0 * x0)))

	elif a == x0 == x2 and b == x1:
		area = 1/2 * abs(((x2 * y1) + (x1 * 0) + (x1 * 0) + (x2 * y2) - (y2 * x1) - (y1 * x1) - (0 * x2) - (0 * x2)))
	
	elif a == x1 == x3 and b == x2:
		area = 1/2 * abs(((x3 * y2) + (x2 * 0) + (x2 * 0) + (x3 * y3) - (y3 * x2) - (y2 * x2) - (0 * x3) - (0 * x3)))
 
	elif a == x1 and b == x0:
		area = (1/2) * abs(((x0 * y1) + (x1 * 0) + (x1 * 0) + (x0 * y0) - (y0 * x1) - (y1 * x1) - (0 * x0) - (0 * x0)))

	elif a == x2 and b == x0:
		area = (1/2) * abs(((x0 * y1) + (x1 * y2) + (x2 * 0) + (x2 * 0) + (x0 * y0) - (y0 * x1) - (y1 * x2) - (y2 * x2) - (0 * x0) - (0 * x0)))

	elif a == x3 and b == x0:
		area = (1/2) * abs(((x0 * y1) + (x1 * y2) + (x2 * y3) + (x3 * 0) + (x3 * 0) + (x0 * y0) - (y0 * x1) - (y1 * x2) - (y2 * x3) - (y3 * x3) - (0 * x0) - (0 * x0)))

	elif a == x0 and b == x1:
		area = (1/2) * abs(((x1 * y2) + (x2 * y3) + (x3 * y0) + (x0 * 0) + (x0 * 0) + (x1 * y1) - (y1 * x2) - (y2 * x3) - (y3 * x0) - (y0 * x0) - (0 * x1) - (0 * x1)))	

	elif a == x2 and b == x1:
		area = (1/2) * abs(((x1 * y2) + (x2 * 0) + (x2 * 0) + (x1 * y1) - (y1 * x2) - (y2 * x2) - (0 * x1) - (0 * x1)))

	elif a == x3 and b == x1:
		area = (1/2) * abs(((x1 * y2) + (x2 * y3) + (x3 * 0) + (x3 * 0) + (x1 * y1) - (y1 * x2) - (y2 * x3) - (y3 * x3) - (0 * x1) - (0 * x1)))

	elif a == x0 and b == x2:
		area = (1/2) * abs(((x2 * y3) + (x3 * y0) + (x0 * 0) + (x0 * 0) + (x2 * y2) - (y2 * x3) - (y3 * x0) - (y0 * x0) - (0 * x2) - (0 * x2)))

	elif a == x1 and b == x2:
		area = (1/2) * abs(((x2 * y3) + (x3 * y0) + (x0 * y1) + (x1 * 0) + (x1 * 0) + (x2 * y2) - (y2 * x3) - (y3 * x0) - (y0 * x1) - (y1 * x1) - (0 * x2) - (0 * x2)))		

	elif a == x3 and b == x2:
		area = (1/2) * abs(((x2 * y3) + (x3 * 0) + (x3 * 0) + (x2 * y2) - (y2 * x3) - (y3 * x3) - (0 * x2) - (0 * x2)))

	elif a == x0 and b == x3:
		area = (1/2) * abs(((x3 * y0) + (x0 * 0) + (x0 * 0) + (x3 * y3) - (y3 * x0) - (y0 * x0) - (0 * x3) - (0 * x3)))

	elif a == x1 and b == x3:
		area = (1/2) * abs(((x3 * y0) + (x0 * y1) + (x1 * 0) + (x1 * 0) + (x3 * y3) - (y3 * x0) - (y0 * x1) - (y1 * x1) - (0 * x3) - (0 * x3)))	

	elif a == x2 and b == x3:
		area = (1/2) * abs(((x3 * y0) + (x0 * y1) + (x1 * y2) + (x2 * 0) + (x2 * 0) + (x3 * y3) - (y3 * x0) - (y0 * x1) - (y1 * x2) - (y2 * x2) - (0 * x3) - (0 * x3)))

area = f"{area:.2f}"
print(area)
