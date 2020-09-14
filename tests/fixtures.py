from __future__ import unicode_literals

import logging
import os
import pytest
import easysnmp

# Disable logging for the C interface
snmp_logger = logging.getLogger('easysnmp.interface')
snmp_logger.disabled = True


SNMP_HOST = os.getenv("SNMP_HOST", "localhost")
SNMP_REMOTE_PORT = int(os.getenv("SNMP_REMOTE_PORT", 11161))


def sess_v1_args():
    return {
        'version': 1,
        'hostname': SNMP_HOST,
        'remote_port': SNMP_REMOTE_PORT,
        'community': 'public'
    }


def sess_v2_args():
    return {
        'version': 2,
        'hostname': SNMP_HOST,
        'remote_port': SNMP_REMOTE_PORT,
        'community': 'public'
    }


def sess_v3_args():
    return {
        'version': 3,
        'hostname': SNMP_HOST,
        'remote_port': SNMP_REMOTE_PORT,
        'security_level': 'authPriv',
        'security_username': 'initial',
        'privacy_password': 'priv_pass',
        'auth_password': 'auth_pass'
    }


def sess_v1():
    return easysnmp.Session(**sess_v1_args())


def sess_v2():
    return easysnmp.Session(**sess_v2_args())


def sess_v3():
    return easysnmp.Session(**sess_v3_args())
