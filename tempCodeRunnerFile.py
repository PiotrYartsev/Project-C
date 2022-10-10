     where_points=sorted(where_points)
        where_points2=where_points.copy()
        resulting_points.append(where_points2)        
        if len(where_points)==n:
            print(where_points)
            pass
        else:
            n=len(where_points)
            #print(n)