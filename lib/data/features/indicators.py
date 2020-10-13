import ta


def add_indicators(df):
    df2=df.copy()
    dataset = ta.add_all_ta_features(df, 'Open', 'High', 'Low', 'Close', 'Volume BTC', fillna=True)
    df2['RSI'] = dataset['momentum_rsi']
    df2['MFI'] = dataset['momentum_mfi']
    df2['TSI'] = dataset['momentum_tsi']
    df2['UO'] = dataset['momentum_uo']
    df2['AO'] = dataset['momentum_ao']

    df2['MACD_diff'] = dataset['trend_macd_diff']
    df2['Vortex_pos'] = dataset['trend_vortex_ind_pos']
    df2['Vortex_neg'] = dataset['trend_vortex_ind_neg']
    df2['Vortex_diff'] = dataset['trend_vortex_ind_diff']
    df2['Trix'] = dataset['trend_trix']
    df2['Mass_index'] = dataset['trend_mass_index']
    df2['CCI'] = dataset['trend_cci']
    df2['DPO'] = dataset['trend_dpo']
    df2['KST'] = dataset['trend_kst']
    df2['KST_sig'] = dataset['trend_kst_sig']
    df2['KST_diff'] = dataset['trend_kst_diff']
    df2['Aroon_up'] = dataset['trend_aroon_up']
    df2['Aroon_down'] = dataset['trend_aroon_down']
    df2['Aroon_ind'] = dataset['trend_aroon_ind']

    df2['BBH'] = dataset['volatility_bbh']
    df2['BBL'] = dataset['volatility_bbl']
    df2['BBM'] = dataset['volatility_bbm']
    df2['BBHI'] = dataset['volatility_bbhi']
    df2['BBLI'] = dataset['volatility_bbli']
    df2['KCHI'] = dataset['volatility_kchi']
    df2['KCLI'] = dataset['volatility_kcli']
    df2['DCHI'] = dataset['volatility_dch']
    df2['DCLI'] = dataset['volatility_dcl']
    df2['ADI'] = dataset['volume_adi']
    df2['OBV'] = dataset['volume_obv']
    df2['CMF'] = dataset['volume_cmf']
    df2['FI'] = dataset['volume_fi']
    df2['EM'] = dataset['volume_em']
    df2['VPT'] = dataset['volume_vpt']
    df2['NVI'] = dataset['volume_nvi']

    df2['DR'] = dataset['others_dr']
    df2['DLR'] = dataset['others_dlr']

    df2.fillna(method='bfill', inplace=True)

    return df2
