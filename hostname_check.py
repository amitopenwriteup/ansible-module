#!/usr/bin/python
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule
import socket

def main():
    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    
    try:
        # Get hostname using socket
        hostname = socket.gethostname()
        
        # Return success with hostname information
        module.exit_json(
            changed=False,
            hostname=hostname,
            msg=f"Hostname (Python): {hostname}"
        )
    
    except Exception as e:
        # Return failure if something goes wrong
        module.fail_json(msg=f"Failed to get hostname: {str(e)}")

if __name__ == "__main__":
    main()
