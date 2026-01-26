# Extended Translation Dictionary for Full Platform Localization
# This file contains comprehensive EN/RU translations for ALL UI elements

EXTENDED_TRANSLATIONS = {
    'en': {
        # Bloch Sphere Module
        'bloch_module_title': 'MODULE 02: HILBERT SPACE MAPPING & BLOCH VECTOR DYNAMICS',
        'bloch_status': 'COHERENCE: OPTIMIZED | FIDELITY: >99.9%',
        'bloch_math_title': 'MATHEMATICAL FORMALISM: PROJECTIVE HILBERT SPACE',
        'bloch_math_intro': 'A single qubit resides within the two-dimensional complex Hilbert space $\\mathcal{H}_2 = \\mathbb{C}^2$. The most general pure state exists as a superposition over the computational basis $\\{|0\\rangle, |1\\rangle\\}$, constrained by the normalization condition inherent to quantum mechanics:',
        'bloch_manifold_title': 'Bloch Sphere Manifold:',
        'bloch_manifold_text': 'The projective Hilbert space $\\mathbb{CP}^1 \\cong S^2$ (Riemann sphere) provides a geometric visualization where each pure state $|\\psi\\rangle$ corresponds to a unique point on the unit sphere. The <strong>Bloch vector</strong> $\\vec{r} = (\\sin\\theta\\cos\\phi, \\sin\\theta\\sin\\phi, \\cos\\theta)$ encodes the state\'s expectation values $\\langle \\sigma_x \\rangle, \\langle \\sigma_y \\rangle, \\langle \\sigma_z \\rangle$.',
        'bloch_pure_states': 'Pure States:',
        'bloch_mixed_states': 'Mixed States:',
        'bloch_maximally_mixed': 'Maximally Mixed:',
        'bloch_surface': 'sphere surface',
        'bloch_interior': 'interior volume, density matrix',
        'bloch_center': 'sphere center',
        
        'bloch_config_title': 'STATE VECTOR CONFIGURATION',
        'bloch_config_desc': 'Manipulate spherical coordinates to observe <strong>geometric phase accumulation</strong> via parallel transport on the Bloch manifold.',
        'bloch_theta_label': '⚛ POLAR ANGLE θ [0, π]',
        'bloch_phi_label': '⚡ AZIMUTHAL PHASE φ [0, 2π] - ROTARY CONTROL',
        'bloch_theta_help': 'Controls latitude on Bloch sphere (|0⟩ at θ=0, |1⟩ at θ=π)',
        'bloch_phi_help': 'Determines relative phase between computational basis states',
        'bloch_gate_sequence_title': 'UNITARY GATE SEQUENCE APPLICATION',
        
        # Common labels
        'label_radians': 'rad',
        'label_degrees': '°',
        'label_coordinates': 'Cartesian Coordinates',
        'label_probability': 'Probability',
        'label_amplitude': 'Amplitude',
        'label_phase': 'Phase',
        'label_fidelity': 'Fidelity',
        'label_purity': 'Purity',
        
        # Buttons
        'button_apply': 'Apply',
        'button_reset': 'Reset',
        'button_export': 'Export',
        'button_run': 'Run',
        'button_visualize': 'Visualize',
        'button_simulate': 'Simulate',
        'button_download': 'Download',
        
        # Status messages
        'status_running': 'Running...',
        'status_complete': 'Complete',
        'status_error': 'Error',
        'status_ready': 'Ready',
        'status_loading': 'Loading...',
        
        # Chart labels
        'chart_probability_distribution': 'Probability Distribution',
        'chart_state_vector': 'State Vector',
        'chart_bloch_sphere': 'Bloch Sphere Visualization',
        'chart_energy_landscape': 'Energy Landscape',
        'chart_convergence': 'Convergence Plot',
        
        # Units
        'unit_percentage': '%',
        'unit_hz': 'Hz',
        'unit_mhz': 'MHz',
        'unit_us': 'μs',
        'unit_ns': 'ns',
        'unit_mk': 'mK',
        
        # Module-specific content will be added dynamically
    },
    'ru': {
        # Bloch Sphere Module
        'bloch_module_title': 'МОДУЛЬ 02: ОТОБРАЖЕНИЕ ПРОСТРАНСТВА ГИЛЬБЕРТА И ДИНАМИКА ВЕКТОРА БЛОХА',
        'bloch_status': 'КОГЕРЕНТНОСТЬ: ОПТИМИЗИРОВАНА | ТОЧНОСТЬ: >99.9%',
        'bloch_math_title': 'МАТЕМАТИЧЕСКИЙ ФОРМАЛИЗМ: ПРОЕКТИВНОЕ ПРОСТРАНСТВО ГИЛЬБЕРТА',
        'bloch_math_intro': 'Один кубит находится в двумерном комплексном пространстве Гильберта $\\mathcal{H}_2 = \\mathbb{C}^2$. Наиболее общее чистое состояние существует как суперпозиция над вычислительным базисом $\\{|0\\rangle, |1\\rangle\\}$, ограниченная условием нормировки, присущим квантовой механике:',
        'bloch_manifold_title': 'Многообразие Сферы Блоха:',
        'bloch_manifold_text': 'Проективное пространство Гильберта $\\mathbb{CP}^1 \\cong S^2$ (сфера Римана) обеспечивает геометрическую визуализацию, где каждое чистое состояние $|\\psi\\rangle$ соответствует уникальной точке на единичной сфере. <strong>Вектор Блоха</strong> $\\vec{r} = (\\sin\\theta\\cos\\phi, \\sin\\theta\\sin\\phi, \\cos\\theta)$ кодирует средние значения состояния $\\langle \\sigma_x \\rangle, \\langle \\sigma_y \\rangle, \\langle \\sigma_z \\rangle$.',
        'bloch_pure_states': 'Чистые Состояния:',
        'bloch_mixed_states': 'Смешанные Состояния:',
        'bloch_maximally_mixed': 'Максимально Смешанные:',
        'bloch_surface': 'поверхность сферы',
        'bloch_interior': 'внутренний объем, матрица плотности',
        'bloch_center': 'центр сферы',
        
        'bloch_config_title': 'КОНФИГУРАЦИЯ ВЕКТОРА СОСТОЯНИЯ',
        'bloch_config_desc': 'Манипулируйте сферическими координатами для наблюдения <strong>накопления геометрической фазы</strong> через параллельный перенос на многообразии Блоха.',
        'bloch_theta_label': '⚛ ПОЛЯРНЫЙ УГОЛ θ [0, π]',
        'bloch_phi_label': '⚡ АЗИМУТАЛЬНАЯ ФАЗА φ [0, 2π] - РОТОРНОЕ УПРАВЛЕНИЕ',
        'bloch_theta_help': 'Управляет широтой на сфере Блоха (|0⟩ при θ=0, |1⟩ при θ=π)',
        'bloch_phi_help': 'Определяет относительную фазу между базисными состояниями',
        'bloch_gate_sequence_title': 'ПРИМЕНЕНИЕ ПОСЛЕДОВАТЕЛЬНОСТИ УНИТАРНЫХ ГЕЙТОВ',
        
        # Common labels
        'label_radians': 'рад',
        'label_degrees': '°',
        'label_coordinates': 'Декартовы Координаты',
        'label_probability': 'Вероятность',
        'label_amplitude': 'Амплитуда',
        'label_phase': 'Фаза',
        'label_fidelity': 'Точность',
        'label_purity': 'Чистота',
        
        # Buttons
        'button_apply': 'Применить',
        'button_reset': 'Сбросить',
        'button_export': 'Экспортировать',
        'button_run': 'Запустить',
        'button_visualize': 'Визуализировать',
        'button_simulate': 'Симулировать',
        'button_download': 'Скачать',
        
        # Status messages
        'status_running': 'Выполняется...',
        'status_complete': 'Завершено',
        'status_error': 'Ошибка',
        'status_ready': 'Готово',
        'status_loading': 'Загрузка...',
        
        # Chart labels
        'chart_probability_distribution': 'Распределение Вероятностей',
        'chart_state_vector': 'Вектор Состояния',
        'chart_bloch_sphere': 'Визуализация Сферы Блоха',
        'chart_energy_landscape': 'Энергетический Ландшафт',
        'chart_convergence': 'График Сходимости',
        
        # Units
        'unit_percentage': '%',
        'unit_hz': 'Гц',
        'unit_mhz': 'МГц',
        'unit_us': 'мкс',
        'unit_ns': 'нс',
        'unit_mk': 'мК',
    }
}
