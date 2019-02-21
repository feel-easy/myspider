from faker import Factory

fake = Factory().create('zh_CN')
print(fake.address())
# print(dir(fake))
print(fake.url())
print(fake.chrome())