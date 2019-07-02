'''import angr

project = angr.Project("./catflag")

#@project.hook(0x400ae4)
bad_addr = 0x080488D7
@project.hook(0x08048869)
def print_flag(state):
    print("INPUT SHOULD BE:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()'''

import angr

proj = angr.Project("./catflag")

# puts("Correct!")0x40073E
target_addr = 0x08048876
bad_addr = 0x080488D7
state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)
simgr.explore(find=target_addr, avoid=bad_addr)
state = simgr.found[0]
print(state.posix.dumps(0))
