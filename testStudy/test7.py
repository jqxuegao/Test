from testStudy.test6 import TestLog

log = TestLog().getlog()

try:
    a = []
    a + 1 == 2
except Exception as msg:
    log.error("异常原因 [ %s ]" % msg)
    raise