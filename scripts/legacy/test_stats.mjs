import assert from 'node:assert/strict';
import {
  mean, median, quantile, variance, pearson, linearRegression, normalCDF,
  binomialPMF, poissonPMF, studentTCDF, regularizedGammaQ, tCritical
} from '../assets/js/stats-core.js';

const close = (actual, expected, tolerance = 1e-6) => assert.ok(Math.abs(actual - expected) <= tolerance, `${actual} is not within ${tolerance} of ${expected}`);

close(mean([1,2,3,4]), 2.5);
close(median([4,1,3,2]), 2.5);
close(quantile([1,2,3,4,5], .25), 2);
close(variance([1,2,3,4,5], true), 2.5);
close(pearson([1,2,3],[2,4,6]), 1);
const model = linearRegression([1,2,3],[3,5,7]);
close(model.slope, 2);
close(model.intercept, 1);
close(model.r2, 1);
close(normalCDF(0), .5, 1e-7);
close(binomialPMF(10,.5,5), .24609375, 1e-10);
close(poissonPMF(3,2), .224041807655, 1e-10);
close(studentTCDF(0,10), .5, 1e-10);
close(regularizedGammaQ(.5,3.841458820694/2), .05, 2e-4);
close(tCritical(.95,10), 2.228138852, 1e-6);
close(tCritical(.95,1), 12.706204736, 1e-5);
console.log('All statistical core tests passed.');
