# 14 — Time Series Forecasting

> **Goal:** Forecast future values from historical data, correctly handling trend, seasonality and the special evaluation rules time series demands.

**Level:** Applied · **Time:** 2 weeks · **Prerequisites:** 07, 09, 11

---

## Learning Objectives
- Decompose and characterize time series (trend, seasonality, noise, stationarity)
- Build classical statistical forecasters and modern ML-based forecasters
- Evaluate forecasts with the correct backtesting methodology
- Forecast at scale across many related series

---

## 14.1 Time Series Fundamentals
- Components: trend, seasonality, cyclical patterns, noise/residual
- **Stationarity**: what it means and why many models need it
- Differencing to achieve stationarity
- Autocorrelation (ACF) and partial autocorrelation (PACF) plots
- Decomposition: additive vs multiplicative (classical decomposition, STL)
- Unit root tests (ADF, KPSS) — awareness

## 14.2 Classical Statistical Models
- Naive and seasonal-naive baselines (always start here)
- Moving averages, exponential smoothing
- **Holt-Winters** (triple exponential smoothing: level, trend, seasonality)
- **ARIMA** (AutoRegressive Integrated Moving Average): the AR, I, MA components
- **SARIMA** (seasonal ARIMA), SARIMAX (with exogenous variables)
- Choosing (p, d, q) orders with ACF/PACF and auto-ARIMA

## 14.3 Feature-Based / ML Approaches
- Reframing forecasting as supervised learning: lag features, rolling statistics, calendar features (link to Section 05.5)
- Gradient boosting for forecasting (often a strong, simple baseline)
- Direct vs recursive multi-step forecasting strategies
- Global models: one model trained across many related series (vs one model per series)

## 14.4 Modern & Specialized Libraries
- **Prophet** (trend + seasonality + holidays, easy to use, good baseline)
- **statsmodels** (ARIMA/SARIMAX, exponential smoothing)
- **Nixtla ecosystem**: StatsForecast, MLForecast, NeuralForecast (fast, scalable, many series at once)
- **Darts** (unified API across many forecasting model types)
- Foundation models for time series (TimeGPT, Chronos, Moirai) — awareness of the emerging pretrained-forecaster space

## 14.5 Deep Learning for Forecasting (bridge)
- RNN/LSTM-based forecasting (concept; full treatment in the deep learning folder)
- Temporal Convolutional Networks
- Transformer-based forecasters (Temporal Fusion Transformer, PatchTST) — awareness

## 14.6 Multivariate & Hierarchical Forecasting
- Multiple related series (e.g. sales per store)
- Hierarchical/grouped time series and reconciliation (top-down, bottom-up, MinT)
- Exogenous variables and their leakage risk (must be known in advance at forecast time)

## 14.7 Evaluation & Backtesting
- Why random k-fold CV is wrong for time series
- **Rolling-origin / walk-forward validation**, expanding vs sliding windows
- Metrics: MAE, RMSE, MAPE, sMAPE, MASE (scaled, comparable across series)
- Forecast intervals / prediction uncertainty
- Comparing against the naive baseline as a sanity check

## 14.8 Production Concerns
- Forecast reconciliation and hierarchy consistency
- Retraining cadence, handling regime changes (e.g. COVID-like shocks)
- Cold-start forecasting (new products/stores with no history)

---

## Hands-on Exercises
1. Decompose a real time series (e.g. retail sales) into trend, seasonality and residual with STL.
2. Fit Holt-Winters, SARIMA and a gradient-boosted model with lag features on the same series; compare with MASE.
3. Implement walk-forward validation from scratch and show why it gives different (more honest) results than k-fold CV.
4. Forecast 100+ related series with MLForecast and compare a global model to per-series models.

## Project — Demand Forecasting Pipeline
Build an end-to-end forecaster for a retail or energy demand dataset: EDA + decomposition, a naive baseline, a classical model (SARIMA or Prophet), an ML model (lag-feature gradient boosting), walk-forward evaluation with MASE, and prediction intervals. Deliver a report comparing all models and recommending one for production.

## Recommended Resources
- *Forecasting: Principles and Practice* (Hyndman & Athanasopoulos) — free online, the standard reference
- Nixtla documentation and tutorials
- Prophet documentation

## Definition of Done
- [ ] Evaluated with walk-forward validation, not random splits
- [ ] Beats the naive/seasonal-naive baseline (or you can explain why it doesn't)
