temperature = input("����������� ���� 20 �������� � ������ 30? (��/���): ")

if temperature == "��":
    is_rainy = input("���� ������? (��/���): ")
    
    if is_rainy == "��":
        print("��������, ����� � ��������")
    else:
        print("�������� � �����")
        
else:
    temperature = input("����������� ���� 0? (��/���): ")
    
    if temperature == "���":
        print("�������")
    else:
        is_rainy = input("���� ������? (��/���): ")
        
        if is_rainy == "��":
            is_raining_heavily = input("������ �������? (��/���): ")
            
            if is_raining_heavily == "��":
                print("������, ��������� ������ � ����")
            else:
                print("������ � ��������")
        else:
            print("������")