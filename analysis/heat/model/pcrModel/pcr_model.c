typedef struct
{
    ThermalModelMatrixCoefficient2x2_t matrixA;
    ThermalModelMatrixCoefficient2x2_t matrixB;
    ThermalModelMatrixCoefficient1x2_t matrixC;
    ThermalModelMatrixCoefficient1x2_t matrixD;
    float C4;
    float C8;
} ThermalModelCoefficients_t;

typedef struct
{
    float sampleEnergy; /* The predicted energy of the sample */
    float airAboveSampleEnergy; /* The predicted energy of the air above the sample */
    float lastResult;
} ThermalModelState_t;

typedef struct
{
    double k00;
    double k10;
} ThermalModelMatrixCoefficient2x1_t;


static void _init(void)
{
    model->coefficients.matrixA = _init2x2Matrix(9.339576155866616e-01, 8.667087146945364e-03, 2.563294914394420e-02, 9.907915439872088e-01);
    model->coefficients.matrixB = _init2x2Matrix(8.012965733670196e-02, 9.200039683698740e-06, 1.062049868559448e-03, 2.113208382023629e-03);
    model->coefficients.matrixC = _init1x2Matrix(2.162230347027591e-01, 9.690098013742272e-04);
    model->coefficients.matrixD = _init1x2Matrix(8.958768040931517e-03, 1.028595706422302e-06);
    model->coefficients.C4 = 0.443;
    model->coefficients.C8 = 1.312;

    model->name = "Thumper Machine-New Cup-1.07mm 9/15/2022";

    model->isPcr = isPcr;
    model->startupTempC = startupTempC;
    model->state.sampleEnergy = startupTempC * model->coefficients.C4;
    model->state.airAboveSampleEnergy = startupTempC * model->coefficients.C8;
    thermalModelUpdate(model, startupTempC, startupTempC, startupTempC);
}



static double _pcrModelCalculate(ThermalModel_t* model, double currentThermistorTempC, double currentAmbientTempC)
{
    ThermalModelCoefficients_t* coefficients = &model->coefficients;
    ThermalModelState_t* state = &model->state;

    ThermalModelMatrixCoefficient2x1_t XX;
    XX.k00 = state->sampleEnergy;
    XX.k10 = state->airAboveSampleEnergy;
    ThermalModelMatrixCoefficient2x1_t U;
    U.k00 = currentThermistorTempC; // * THERMAL_MODEL_C4;
    U.k10 = currentAmbientTempC; // * THERMAL_MODEL_C8;

    XX = _matrixAdd2x1and2x1(_matrixMultiply2x2by2x1(coefficients->matrixA, XX), _matrixMultiply2x2by2x1(coefficients->matrixB, U));
    state->sampleEnergy = XX.k00;
    state->airAboveSampleEnergy = XX.k10;

    return (_matrixMultiply1x2by2x1(coefficients->matrixC, XX) + _matrixMultiply1x2by2x1(coefficients->matrixD, U)) / coefficients->C4;
}


static ThermalModelMatrixCoefficient2x1_t _matrixMultiply2x2by2x1(ThermalModelMatrixCoefficient2x2_t m22, ThermalModelMatrixCoefficient2x1_t m21)
{
    ThermalModelMatrixCoefficient2x1_t returnMatrix;
    returnMatrix.k00 = (m22.k00 * m21.k00) + (m22.k01 * m21.k10);
    returnMatrix.k10 = (m22.k10 * m21.k00) + (m22.k11 * m21.k10);
    return returnMatrix;
}



static ThermalModelMatrixCoefficient2x1_t _matrixAdd2x1and2x1(ThermalModelMatrixCoefficient2x1_t m21_1, ThermalModelMatrixCoefficient2x1_t m21_2)
{
    ThermalModelMatrixCoefficient2x1_t returnMatrix;
    returnMatrix.k00 = m21_1.k00 + m21_2.k00;
    returnMatrix.k10 = m21_1.k10 + m21_2.k10;
    return returnMatrix;
}



static double _matrixMultiply1x2by2x1(ThermalModelMatrixCoefficient1x2_t m12, ThermalModelMatrixCoefficient2x1_t m21)
{
    return (m12.k00 * m21.k00) + (m12.k01 * m21.k10);
}