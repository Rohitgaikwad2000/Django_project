from app.models import Product
# exec(open(r'F:\Python(Rohit)\Django_projects\productapp\app\db_shell.py').read())

# Product.objects.create(Name="ABC", MF_date = "2020-3-19",
#                        product_no = "123")


# p1 = Product.objects.create(Name="xyz", MF_date = "2023-5-29",
#                        product_no = "569")
# p1.save()


# Product.objects.create(Name="por", MF_date = "2022-8-23",
#                        product_no = "183")


# Product.objects.create(Name="efd", MF_date = "2018-6-14",
#                        product_no = "236")


# p1 = Product.objects.create(Name="lmn", MF_date = "2016-2-23",
#                        product_no = "236")
# p1.save()


# ---------------------------------

# p1 = Product.objects.all()
# print(p1)

# for i in p1:
    # print(i.MF_date)


# print(Product.objects.get(id = 2))


# p1 = Product.objects.get(id = 3)
# p1.Name = "Rst"
# print(p1)


# Product.objects.get(id = 3).delete()


# p1 = Product.objects.filter(Name__startswith="A").order_by("id")
# print(p1)



# p1 = Product.objects.filter(id__in=[12,14]).delete()            # delete using bt id(using in operator)
# print(p1)
# print("success")

