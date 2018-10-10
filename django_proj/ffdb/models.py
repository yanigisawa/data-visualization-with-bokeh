from django.db import models


class PlayerStat(models.Model):
    player_name = models.CharField(max_length=200, blank=True, null=True)
    nfl = models.CharField(max_length=3, blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=2, blank=True, null=True)
    plays = models.IntegerField(blank=True, null=True)
    fpts = models.IntegerField(blank=True, null=True)
    gp = models.IntegerField(blank=True, null=True)
    fpts_per_game = models.IntegerField(blank=True, null=True)
    run = models.IntegerField(blank=True, null=True)
    ryd = models.IntegerField(blank=True, null=True)
    rtd = models.IntegerField(blank=True, null=True)
    pass_count = models.IntegerField(blank=True, null=True)
    cmp = models.IntegerField(blank=True, null=True)
    pyds = models.IntegerField(blank=True, null=True)
    fum = models.IntegerField(blank=True, null=True)
    fg = models.IntegerField(blank=True, null=True)
    fg_miss = models.IntegerField(blank=True, null=True)
    xpt = models.IntegerField(blank=True, null=True)
    xpt_miss = models.IntegerField(blank=True, null=True)
    team_defense = models.IntegerField(blank=True, null=True)
    sack = models.IntegerField(blank=True, null=True)
    fr = models.IntegerField(blank=True, null=True)
    int = models.IntegerField(blank=True, null=True)
    td = models.IntegerField(blank=True, null=True)
    sfty = models.IntegerField(blank=True, null=True)
    ryda = models.IntegerField(blank=True, null=True)
    pyda = models.IntegerField(blank=True, null=True)
    tyda = models.IntegerField(blank=True, null=True)
    tkls = models.IntegerField(blank=True, null=True)
    solo = models.IntegerField(blank=True, null=True)
    asst = models.IntegerField(blank=True, null=True)
    sacks = models.IntegerField(blank=True, null=True)
    ff = models.IntegerField(blank=True, null=True)
    rf = models.IntegerField(blank=True, null=True)
    pd = models.IntegerField(blank=True, null=True)
    krtn = models.IntegerField(blank=True, null=True)
    kryd = models.IntegerField(blank=True, null=True)
    kavg = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    klng = models.IntegerField(blank=True, null=True)
    ktd = models.IntegerField(blank=True, null=True)
    prtn = models.IntegerField(blank=True, null=True)
    pryd = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    pavg = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    plng = models.IntegerField(blank=True, null=True)
    ptd = models.IntegerField(blank=True, null=True)
    pfc = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'player_stat'

    def as_dict(self):
        p = self.__dict__
        for k in ['_state', 'id']:
            if k in p.keys():
                del p[k]
        decimals = ['kavg', 'pryd', 'pavg']
        for d in decimals:
            if p[d] is None:
                continue
            p[d] = float(p[d])
        return p
