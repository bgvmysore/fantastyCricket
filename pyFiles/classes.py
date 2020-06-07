"""Classes of Player , Teams , Matches """
import sqlite3


class Players():
    def __init__(self):
        self.conn = ConDB()
        self.p_tuple = self.conn.ret_p()
        return

    def __str__(self):
        self.strg = ''
        for i in self.p_tuple:
            self.strg += str(i) + '\n'
        return self.strg


class Matches():
    def __init__(self, m_id='Match1'):
        self.m_id = m_id
        self.conn = ConDB()
        self.m_tuple = self.conn.ret_m(self.m_id)
        return

    def __str__(self):
        self.strg = ''
        for i in self.m_tuple:
            self.strg += str(i) + '\n'
        return self.strg

    def teamtopid(self, t):
        self.teampid = []
        for i in t.teamlist:
            for ii in self.m_tuple:
                if i[0] == ii[0]:
                    self.teampid += [self.m_tuple.index(ii)]

    def bat_points(self, p_id=0):
        self.p = self.m_tuple[p_id]
        self.runs = self.p[1]
        self.balls = self.p[2]
        self.fours = self.p[3]
        self.sixes = self.p[4]
        self.s = 0
        self.s = self.s+(self.runs/2)
        if self.runs >= 50:
            self.s = self.s+5
        if self.runs >= 100:
            self.s = self.s+10
        if self.balls == 0:
            return self.s
        if (self.runs/self.balls) >= 0.80 and (self.runs/self.balls) <= 1:
            self.s = self.s+2
        if (self.runs/self.balls) > 1:
            self.s = self.s + 4
        self.s = self.s+(self.fours*1)
        self.s = self.s+(self.sixes*2)
        return self.s

    def ball_points(self, p_id=0):
        self.p = self.m_tuple[p_id]
        self.wik = self.p[-4]
        self.ovr = self.p[5]/6
        self.runs = self.p[-5]
        if self.ovr == 0:
            return 0
        self.s = 0
        self.s = self.s+(self.wik*10)
        if self.wik >= 3:
            self.s = self.s+5
        if self.wik >= 5:
            self.s = self.s+10
        if (self.runs/self.ovr) >= 3.5 and (self.runs/self.ovr) <= 4.5:
            self.s = self.s+4
        if (self.runs/self.ovr) >= 2 and (self.runs/self.ovr) < 3.5:
            self.s = self.s+7
        if (self.runs/self.ovr) < 2:
            self.s = self.s+10
        return self.s

    def field_points(self, p_id=0):
        self.p = self.m_tuple[p_id]
        self.fd = self.p[-3]+self.p[-2]+self.p[-1]
        self.s = self.fd*10
        return self.s
        

    def teamscores(self, t1):
        self.teamtopid(t1)
        self.teammatchscore = 0
        self.teamscores_list = []
        for i in self.teampid:
            x1 = self.bat_points(i)
            x2 = self.ball_points(i)
            x3 = self.field_points(i)
            self.teamscores_list += [(x1, x2, x3, x1+x2+x3)]
            self.teammatchscore += x1+x2+x3
        return


class Team:
    maxpoints = 1000
    teams = []

    def __init__(self, plist=None):
        self.build_t(plist)
        tconn = ConDB()
        Team.teams = tconn.listofteams()
        return

    def build_t(self, plist):
        if plist is None:
            return
        if not len(plist) == 11:
            self.teamlist = None
            print("Failed to Build Team")
            return
        self.teamlist = plist
        self.calc_pnt()
        if self.teampoint > Team.maxpoints:
            print("Max Points Exceeded!")
            self.teamlist = None
            return
        self.t_role_cnt()
        if not self.rolecnt[-1] == 1:
            print("Only 1 wkt keeper allowed")
            self.teamlist = None
            return
        print("Team Built!")
        return

    def calc_pnt(self):
        self.teampoint = 0
        for i in self.teamlist:
            self.teampoint += i[-2]
        print(self.teampoint)

    def t_role_cnt(self):
        bat = 0
        bow = 0
        alr = 0
        wkt = 0
        for i in self.teamlist:
            if i[-1] == 'BAT':
                bat += 1
            if i[-1] == 'BWL':
                bow += 1
            if i[-1] == 'AR':
                alr += 1
            if i[-1] == 'WK':
                wkt += 1
        self.rolecnt = bat, bow, alr, wkt

    def __str__(self):
        if self.teamlist is None:
            return "None"
        self.strg = ''
        self.ct = 1
        for i in self.teamlist:
            self.strg += str(self.ct) + str(i) + '\n'
            self.ct += 1
        return self.strg

    def saveTeam(self, team_name):
        self.tn = team_name
        tconn = ConDB()
        try:
            tconn.svtdb(self.teamlist, self.tn)
        except Exception as e:
            print(e)
            import time
            tm = time.strftime('%H_%M_%S')
            self.tn += str(tm)
            tconn.svtdb(self.teamlist, self.tn)
        Team.teams = tconn.listofteams()
        return

    def LoadTeam(self, team_name):
        if team_name in Team.teams:
            self.ind = Team.teams.index(team_name)
            tconn = ConDB()
            self.teamlist = tconn.ldtdb(Team.teams[self.ind])
            self.calc_pnt()
            self.t_role_cnt()
            return
        else:
            print("Team not Found!")
            return


class ConDB():
    def ret_p(self):
        self.db = sqlite3.connect("./db/cricket.db")
        self.cur = self.db.cursor()
        self.cur.execute("SELECT * FROM Players;")
        self.pdata = self.cur.fetchall()
        self.db.close()
        return self.pdata

    def ret_m(self, name ='Match1'):
        self.id = name
        self.db = sqlite3.connect("./db/matches.db")
        self.cur = self.db.cursor() 
        self.cur.execute(f"SELECT * FROM {self.id} ;")
        self.mdata = self.cur.fetchall()
        self.db.close()
        return self.mdata
        
    def listofmatches(self):
        self.db = sqlite3.connect("./db/matches.db")
        self.cur = self.db.cursor()
        self.cur.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        self.mlistall = self.cur.fetchall()
        self.db.close()
        self.mlistall1 = []
        for i in self.mlistall:
            self.mlistall1 += [i[0]]
        return self.mlistall1

    def svtdb(self, ply_list, typ='Team1'):
        self.db = sqlite3.connect("./db/teams.db")
        self.cur = self.db.cursor()
        exec_str = f"""CREATE TABLE {typ} (
                    player TEXT(50) PRIMARY KEY
                                    NOT NULL,
                    points INTEGER,
                    role TEXT(5) );"""
        self.cur.execute(exec_str)
        for i in ply_list:
            self.cur.execute(f"""INSERT INTO {typ} (player,
                             points,role) VALUES (?,?,?);""",
                             (i[0], i[-2], i[-1]))
            self.db.commit()
        self.db.close()

    def ldtdb(self, tname):
        self.db = sqlite3.connect("./db/teams.db")
        self.cur = self.db.cursor()
        self.cur.execute(f"SELECT * FROM {tname};")
        self.tdata = self.cur.fetchall()
        self.db.close()
        return self.tdata

    def listofteams(self):
        self.db = sqlite3.connect("./db/teams.db")
        self.cur = self.db.cursor()
        self.cur.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        self.tlistall = self.cur.fetchall()
        self.db.close()
        self.tlistall1 = []
        for i in self.tlistall:
            self.tlistall1 += [i[0]]
        return self.tlistall1


if __name__ == '__main__':
    p1 = Players()
    ii = 0
    for i in p1.p_tuple:
        print(ii+1, " ", i)
        ii += 1
    selection = 1, 2, 4, 6, 3, 10, 14, 5, 9, 12, 13
    plist1 = []
    for i in selection:
        plist1 += [p1.p_tuple[i-1]]
    print(len(plist1))
    t1 = Team()
    t1.LoadTeam("myteam")
    print(t1)
    print(t1.rolecnt)
    # t1.saveTeam("notmyteam")
    print(t1.teampoint)
    m1 = Matches()
    m1.teamscores(t1)
    print(m1.teammatchscore)
    print('\n', m1.teamscores_list)
    conn = ConDB()
    print(conn.listofmatches())