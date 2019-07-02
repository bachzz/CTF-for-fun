'''import angr

project = angr.Project("reme")

#@project.hook(0x400ae4)
@project.hook(0x400ad4)
def print_flag(state):
    print("FLAG SHOULD BE:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()'''
import angr

proj = angr.Project("./reme")

# puts("Correct!")
bad_addr = [0x400B72, 0x400BBA, 0x40094A, 0x400A08, 0x400AA9]
target_addr = 0x400AD4

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)
simgr.explore(find=target_addr, avoid=bad_addr)
state = simgr.found[0]
print(state.posix.dumps(0))
