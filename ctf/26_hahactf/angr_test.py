import angr

proj = angr.Project("./pwnd")

# puts("Correct!")
target_addr = 0x08048654#0x08048720#0x400720#654
bad_addr = 0x08048671

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)
simgr.explore(find=target_addr, avoid=bad_addr)
state = simgr.found[0]
print(state.posix.dumps(0))
