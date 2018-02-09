#!/usr/bin/python3
import pymysql

# ============================================================================

mysql_user = 'root'
mysql_pass = '123@Qwe!'
mysql_port = 3306
mysql_socket = 'NULL'
mysql_flags = 0
mysql_ssl = 'FALSE' # Whether to use SSL to connect to MySQL.
mysql_ssl_key = '/etc/pki/tls/certs/mysql/client-key.pem'
mysql_ssl_cert = '/etc/pki/tls/certs/mysql/client-cert.pem'
mysql_ssl_ca = '/etc/pki/tls/certs/mysql/ca-cert.pem'
mysql_connection_timeout = 5

heartbeat = 'FALSE'        # Whether to use pt-heartbeat table for repl. delay calculation.
heartbeat_utc = 'FALSE'    # Whether pt-heartbeat is run with --utc option.
heartbeat_server_id = 0    # Server id to associate with a heartbeat. Leave 0 if no preference.
heartbeat_table = 'percona.heartbeat'  # db.tbl.

cache_dir = '/tmp'  # If set, this uses caching to avoid multiple calls.
poll_time = 300     # Adjust to match your polling interval.
timezone = 'null'    # If not set, uses the system default.  Example: "UTC"
chk_options = {
    'innodb': 'true',    # Do you want to check InnoDB statistics?
    'master': 'true',    # Do you want to check binary logging?
    'slave': 'true',    # Do you want to check slave status?
    'procs': 'true',    # Do you want to check SHOW PROCESSLIST?
    'get_qrt': 'true'    # Get query response times from Percona Server or MariaDB?
}
use_ss = 'FAL SE'  # Whether to use the script server or not
debug = 'FALSE'  # Define whether you want debugging behavior.
debug_log = 'FALSE'  # If $debug_log is a filename, it'll be used.

# ============================================================================

def _Conn():
    conn = pymysql.Connect(host='10.86.15.22', port=3306, user=mysql_user, passwd=mysql_pass, db='mysql', charset='utf8')
    cursor = conn.cursor()
    return cursor

def Runsql(sql):
    cur = _Conn()
    cur.execute(sql)
    return cur

if __name__ == "__main__":
    result = Runsql("show processlist;")
    for each in result.fetchall():
        print(each)
    result.close()

    Mysql_version = Runsql("select version();").fetchall()
    print(Mysql_version)

  $status = array( # Holds the result of SHOW STATUS, SHOW INNODB STATUS, etc
 # Define some indexes so they don't cause errors with += operations.
	'relay_log_space'          => null,
	'binary_log_space'         => null,
	'current_transactions'     => 0,
	'locked_transactions'      => 0,
	'active_transactions'      => 0,
	'innodb_locked_tables'     => 0,
	'innodb_tables_in_use'     => 0,
	'innodb_lock_structs'      => 0,
	'innodb_lock_wait_secs'    => 0,
	'innodb_sem_waits'         => 0,
	'innodb_sem_wait_time_ms'  => 0,
	# Values for the 'state' column from SHOW PROCESSLIST (converted to
	# lowercase, with spaces replaced by underscores)
	'State_closing_tables'       => 0,
	'State_copying_to_tmp_table' => 0,
	'State_end'                  => 0,
	'State_freeing_items'        => 0,
	'State_init'                 => 0,
	'State_locked'               => 0,
	'State_login'                => 0,
	'State_preparing'            => 0,
	'State_reading_from_net'     => 0,
	'State_sending_data'         => 0,
	'State_sorting_result'       => 0,
	'State_statistics'           => 0,
	'State_updating'             => 0,
	'State_writing_to_net'       => 0,
	'State_none'                 => 0,
	'State_other'                => 0, # Everything not listed above
   );













