from reporter.header import create_header

def test_create_header():
    auth_list =[
        {"first" : "Jean", "last" : "Dupont"},
        {"first" : "Eric", "last" : "Martin"},
    ]
    
    res = create_header(auth_list,"NY")
    if not "Jean" in res:
        raise ValueError ('Prénom manquant')
        
    assert "NY" in res
        
test_create_header()