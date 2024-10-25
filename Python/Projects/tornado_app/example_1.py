import asyncio

# Notes:
# A Function marked as async, is a coroutine and must be called with await or passed to the event loop for execution.


async def divide(x, y):
    return x / y


def bad_call():
    print (divide(1, 0))        # missing await


#asyncio.run(bad_call())         # calling a coroutine just returns a coroutine object, not actual execution and error is trapped
print("\n")


# Example - 1 - coroutine with await:

async def good_call():
    print (await divide(1, 0))


#asyncio.run(good_call())



# Example - 2 - coroutine with Event-Loop:

async def addition(x, y):
    return x + y

# Works
loop = asyncio.get_event_loop()
result = loop.run_until_complete(addition(10, 20))
loop.close()
print("\nresult from event loop is = ", result)


# Not Working, because of exception loop will be closed and it will not return/print the correct exception [exception trapping]
loop1 = asyncio.get_event_loop()
result1 = loop1.run_until_complete(addition(10, "Hello"))
loop1.close()
print(result1)

