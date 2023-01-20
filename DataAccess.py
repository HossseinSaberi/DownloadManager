import sqlite3


class ConnectToDB:
    def __init__(self):
        self.create_table()

    def create_conn(self):
        with sqlite3.connect('DownloadManager.db') as database_connection:
            return database_connection

    def drop_table(self):
        conn = self.create_conn()
        cur = conn.cursor()
        query = "DROP TABLE download_manager"
        cur.execute(query)

    def create_table(self):
        conn = self.create_conn()
        cur = conn.cursor()
        query = "CREATE TABLE IF NOT EXISTS download_manager (dmid INTEGER PRIMARY KEY AUTOINCREMENT, file_name TEXT , file_extention TEXT , download_date TEXT , download_time TEXT , download_status)"
        cur.execute(query)

    def select_last_file_of_extention(self, extention):
        conn = self.create_conn()
        cur = conn.cursor()
        query = "SELECT count(dmid) FROM download_manager WHERE file_extention = '{file_extention}'".format(
            file_extention=extention)
        cur.execute(query)
        max_id = cur.fetchone()
        if not max_id[0]:
            return 1
        return max_id[0] + 1

    def insert_new_download(self, file_name, file_extention, download_date, download_time, download_status):
        conn = self.create_conn()
        cur = conn.cursor()
        query = "INSERT INTO download_manager (file_name , file_extention , download_date , download_time , download_status) VALUES ('{}','{}','{}','{}','{}') RETURNING dmid".format(
            file_name, file_extention, download_date, download_time, download_status)
        print(query) 
        cur.execute(query)
        dmid = cur.fetchone()
        return dmid[0]
        
    def update_downloaded_file_status(self , download_status , dmid , cdate , ctime):
        conn = self.create_conn()
        cur = conn.cursor()
        query = "UPDATE download_manager SET download_status = '{}' , download_date = '{}' , download_time='{}' WHERE dmid = {};".format(download_status , cdate , ctime , dmid)
        print(query) 
        cur.execute(query)
        conn.commit()
        
    # def insert_to_pending_list(self, file_name, file_extention):
    #     cur = self.create_conn()
    #     query = "INSERT INTO download_manager (file_name , file_extention) VALUES ('{}','{}')".format(
    #         file_name, file_extention)
    #     print(query)
    #     cur.execute(query)
    #     self.create_conn().commit()

    def select_from_pending_list(self): 
        conn = self.create_conn()
        cur = conn.cursor()
        query = "SELECT dmid , file_name , file_extention FROM download_manager WHERE download_status = '{}'".format('pending')
        cur.execute(query)
        data = cur.fetchall()
        print(data)
        return data


if __name__ == '__main__':
    x = ConnectToDB()
    x.drop_table()