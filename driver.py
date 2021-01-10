import testing

print('Pasirinkite paleidimo buda:\n0 - Rasti variantus NxN lentoje;\n1 - Greicio analize')

global case
case = int(input(''))

print('\n')

if(case == 0):
    n = int(input('Iveskite lentos dydi: '))

    testing.solve_single(n)

    print('Rezultatai isvesti failuose solution_bishops ir solution_queens.')

elif(case == 1):
    print('Iveskite lentos NxN dydi:')
    n_from = int(input('Pradinis N = '))
    n_to = int(input('Paskutinis N = '))

    testing.solve(n_from, n_to)
